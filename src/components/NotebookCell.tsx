
"use client";

import { useEffect, useRef, useState } from "react";
import type { KeyboardEvent } from "react";

type NotebookOutput = {
  type: string;
  data: string;
};

type NotebookResult = {
  status?: string;
  stdout?: string;
  stderr?: string;
  outputs?: NotebookOutput[];
  execution_time_ms?: number;
};

type Props = {
  questionId: string;
  value: string;
  onChange: (code: string) => void;
};

const API = "http://127.0.0.1:8015";

export default function NotebookCell({
  questionId,
  value,
  onChange,
}: Props) {
  const [running, setRunning] = useState(false);
  const [result, setResult] = useState<NotebookResult | null>(null);
  const [error, setError] = useState("");
  const [executionCount, setExecutionCount] = useState(0);

  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const requestRef = useRef(0);

  // Clear notebook output when switching questions.
  useEffect(() => {
    requestRef.current += 1;
    setResult(null);
    setError("");
    setRunning(false);
    setExecutionCount(0);
  }, [questionId]);

  async function runCell() {
    if (running || !value.trim()) return;

    const requestId = ++requestRef.current;

    setRunning(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(`${API}/api/notebook/execute`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question_id: questionId,
          code: value,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        const detail = data?.detail;

        throw new Error(
          typeof detail === "string"
            ? detail
            : `Jupyter execution failed: HTTP ${response.status}`
        );
      }

      if (requestId !== requestRef.current) return;

      setResult(data as NotebookResult);
      setExecutionCount((previous) => previous + 1);
    } catch (err) {
      if (requestId !== requestRef.current) return;

      setError(
        err instanceof Error
          ? err.message
          : "Unable to execute the Python cell."
      );
    } finally {
      if (requestId === requestRef.current) {
        setRunning(false);
      }
    }
  }

  function replaceSelection(
    editor: HTMLTextAreaElement,
    start: number,
    end: number,
    inserted: string,
    cursorOffset = inserted.length
  ) {
    onChange(value.slice(0, start) + inserted + value.slice(end));
    requestAnimationFrame(() => {
      editor.focus();
      editor.setSelectionRange(start + cursorOffset, start + cursorOffset);
    });
  }

  function handleKeyDown(event: KeyboardEvent<HTMLTextAreaElement>) {
    const editor = event.currentTarget;
    const start = editor.selectionStart;
    const end = editor.selectionEnd;
    const lineStart = value.lastIndexOf("\n", start - 1) + 1;
    const beforeCursor = value.slice(lineStart, start);
    const indent = (beforeCursor.match(/^[ \t]*/) ?? [""])[0].replace(/\t/g, "    ");

    // Execute this one notebook cell. Never submit it implicitly.
    if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
      event.preventDefault();
      void runCell();
      return;
    }

    // Preserve indentation on Enter. A Python block header adds four spaces.
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      const trimmed = beforeCursor.trimEnd();
      const additionalIndent = trimmed.endsWith(":") && !trimmed.trimStart().startsWith("#")
        ? "    "
        : "";
      replaceSelection(editor, start, end, "\n" + indent + additionalIndent);
      return;
    }

    if (event.key === "Tab") {
      event.preventDefault();
      // Indent or unindent the whole selected block, rather than destroying it.
      if (end > start && value.slice(start, end).includes("\n")) {
        const firstLineStart = value.lastIndexOf("\n", start - 1) + 1;
        const lastLineEnd = value.indexOf("\n", end);
        const blockEnd = lastLineEnd === -1 ? value.length : lastLineEnd;
        const oldBlock = value.slice(firstLineStart, blockEnd);
        const updatedBlock = oldBlock.split("\n").map((line) => {
          if (event.shiftKey) return line.replace(/^( {1,4}|\t)/, "");
          return "    " + line;
        }).join("\n");
        onChange(value.slice(0, firstLineStart) + updatedBlock + value.slice(blockEnd));
        requestAnimationFrame(() => {
          editor.focus();
          editor.setSelectionRange(firstLineStart, firstLineStart + updatedBlock.length);
        });
        return;
      }

      if (event.shiftKey) {
        const removable = (value.slice(lineStart).match(/^( {1,4}|\t)/) ?? [""])[0].length;
        if (removable) {
          onChange(value.slice(0, lineStart) + value.slice(lineStart + removable));
          requestAnimationFrame(() => {
            editor.focus();
            editor.setSelectionRange(Math.max(lineStart, start - removable), Math.max(lineStart, end - removable));
          });
        }
        return;
      }

      replaceSelection(editor, start, end, "    ");
      return;
    }

    // Backspace on a blank indent removes one indentation level.
    if (event.key === "Backspace" && start === end && /^[ ]+$/.test(beforeCursor)) {
      event.preventDefault();
      const removeCount = (beforeCursor.length - 1) % 4 + 1;
      replaceSelection(editor, start - removeCount, start, "");
    }
  }

  const hasOutput =
    Boolean(error) ||
    Boolean(result?.stdout) ||
    Boolean(result?.stderr) ||
    Boolean(result?.outputs?.length) ||
    result !== null;

  return (
    <section
      style={{
        border: "1px solid #d8e0ef",
        borderRadius: 14,
        overflow: "hidden",
        background: "#ffffff",
        width: "100%",
      }}
    >
      {/* Notebook header */}
      <div
        style={{
          background: "#f8fafc",
          padding: "13px 16px",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          gap: 12,
          flexWrap: "wrap",
        }}
      >
        <div>
          <strong
            style={{
              color: "#14213d",
              fontSize: 16,
              display: "block",
            }}
          >
            solution.py
          </strong>

          <span
            style={{
              color: "#64748b",
              fontSize: 12,
            }}
          >
            Python 3 · Jupyter Code Cell
          </span>
        </div>

        <button
          type="button"
          onClick={() => void runCell()}
          disabled={running || !value.trim()}
          style={{
            background: running ? "#8b82ee" : "#6045f5",
            color: "#ffffff",
            border: "none",
            borderRadius: 9,
            padding: "11px 17px",
            fontSize: 14,
            fontWeight: 700,
            cursor: running ? "wait" : "pointer",
            opacity: !value.trim() ? 0.6 : 1,
          }}
        >
          {running ? "Running..." : "▶ Run Cell"}
        </button>
      </div>

      {/* One Python cell */}
      <div
        style={{
          background: "#ffffff",
          display: "flex",
          minHeight: 300,
        }}
      >
        <div
          style={{
            color: "#64748b",
            background: "#f8fafc",
            padding: "19px 10px",
            fontSize: 12,
            fontFamily: "Consolas, monospace",
            whiteSpace: "nowrap",
            borderRight: "1px solid #e2e8f0",
          }}
        >
          {running
            ? "In [*]:"
            : executionCount > 0
              ? `In [${executionCount}]:`
              : "In [ ]:"}
        </div>

        <textarea
          ref={textareaRef}
          aria-label="Jupyter Python code editor"
          value={value}
          onChange={(event) => onChange(event.target.value)}
          onKeyDown={handleKeyDown}
          spellCheck={false}
          autoCapitalize="off"
          autoCorrect="off"
          style={{
            width: "100%",
            minHeight: 300,
            resize: "vertical",
            outline: "none",
            border: "none",
            background: "transparent",
            color: "#24292f",
            padding: "19px 16px",
            fontFamily: "Consolas, 'Courier New', monospace",
            fontSize: 14,
            lineHeight: 1.8,
            tabSize: 4,
          }}
        />
      </div>

      {/* Execution output */}
      {hasOutput && (
        <div
          style={{
            borderTop: "1px solid #d8e0ef",
            background: "#ffffff",
            padding: 16,
          }}
        >
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              flexWrap: "wrap",
              gap: 8,
              marginBottom: 12,
            }}
          >
            <strong
              style={{
                fontSize: 13,
                color: "#334155",
              }}
            >
              Out [{executionCount}]:
            </strong>

            {result && (
              <span
                style={{
                  fontSize: 12,
                  color: "#64748b",
                }}
              >
                {result.status ?? "Completed"}
                {typeof result.execution_time_ms === "number"
                  ? ` · ${result.execution_time_ms} ms`
                  : ""}
              </span>
            )}
          </div>

          {error && (
            <pre
              style={{
                background: "#fff1f2",
                border: "1px solid #fecdd3",
                borderRadius: 8,
                color: "#be123c",
                padding: 13,
                whiteSpace: "pre-wrap",
                overflowWrap: "anywhere",
              }}
            >
              {error}
            </pre>
          )}

          {result?.stdout && (
            <pre
              style={{
                color: "#172033",
                padding: 12,
                background: "#f6f8fc",
                borderRadius: 8,
                whiteSpace: "pre-wrap",
                overflowWrap: "anywhere",
                fontFamily: "Consolas, monospace",
                fontSize: 13,
              }}
            >
              {result.stdout}
            </pre>
          )}

          {result?.stderr && (
            <pre
              style={{
                background: "#fff1f2",
                borderRadius: 8,
                padding: 12,
                color: "#b42318",
                whiteSpace: "pre-wrap",
                overflowWrap: "anywhere",
                fontFamily: "Consolas, monospace",
                fontSize: 13,
              }}
            >
              {result.stderr}
            </pre>
          )}

          {result?.outputs?.map((output, index) => {
            if (output.type === "image/png") {
              return (
                <img
                  key={index}
                  src={`data:image/png;base64,${output.data}`}
                  alt={`Jupyter output ${index + 1}`}
                  style={{
                    display: "block",
                    maxWidth: "100%",
                    height: "auto",
                    marginTop: 12,
                    borderRadius: 8,
                  }}
                />
              );
            }

            return (
              <pre
                key={index}
                style={{
                  background: "#f6f8fc",
                  padding: 12,
                  borderRadius: 8,
                  color: "#172033",
                  whiteSpace: "pre-wrap",
                  overflowWrap: "anywhere",
                  fontFamily: "Consolas, monospace",
                  fontSize: 13,
                }}
              >
                {output.data}
              </pre>
            );
          })}

          {result &&
            !result.stdout &&
            !result.stderr &&
            !result.outputs?.length && (
              <span
                style={{
                  fontSize: 13,
                  color: "#64748b",
                }}
              >
                Executed successfully. No output was produced.
              </span>
            )}
        </div>
      )}

      {/* Footer */}
      <div
        style={{
          padding: "10px 16px",
          borderTop: "1px solid #e2e8f0",
          color: "#64748b",
          fontSize: 12,
        }}
      >
        Ctrl + Enter to run · Enter auto-indents · Tab/Shift+Tab to indent or unindent ·
        Run Code and Submit Code use the same solution.
      </div>
    </section>
  );
}
