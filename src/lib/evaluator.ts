const API_BASE =
  process.env.NEXT_PUBLIC_EVALUATOR_API_URL ||
  "http://127.0.0.1:8015";

export type RunResult = {
  status: string;
  tests_available: boolean;
  score: number;
  passed: number;
  total: number;
  tests: {
    name: string;
    passed: boolean;
    error?: string;
  }[];
  stdout: string;
  stderr: string;
  error: string | null;
  execution_time_ms: number;
};

export async function runCode(
  questionId: string,
  code: string
): Promise<RunResult> {
  const response = await fetch(
    `${API_BASE}/api/run`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        question_id: questionId,
        code,
      }),
    }
  );

  const data = await response.json();

  if (!response.ok) {
    throw new Error(
      data?.detail ||
      "Unable to run the code."
    );
  }

  return data;
}