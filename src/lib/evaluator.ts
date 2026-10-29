
const API_URL = "http://127.0.0.1:8015";

export type TestResult = {
  name: string;
  passed: boolean;
  error?: string | null;
};

export type RunResult = {
  status: string;
  passed: number;
  total: number;
  score: number;
  execution_time_ms: number;
  tests_available?: boolean;
  tests?: TestResult[];
  error?: string | null;
  stdout?: string;
  stderr?: string;
};

export async function runCode(
  questionId: string,
  code: string,
  mode: "run" | "submit" = "run"
): Promise<RunResult> {
  const response = await fetch(`${API_URL}/api/run`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      question_id: questionId,
      code,
      mode,
    }),
  });

  let result: RunResult & { detail?: string };

  try {
    result = await response.json();
  } catch {
    throw new Error(
      `Server returned an invalid response (${response.status}).`
    );
  }

  if (!response.ok) {
    throw new Error(
      typeof result.detail === "string"
        ? result.detail
        : `Code execution failed (${response.status}).`
    );
  }

  return result;
}
