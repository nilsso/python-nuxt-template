export type Method = "GET" | "POST" | "PUT" | "DELETE";

export async function modelRequest(
  model: string,
  action: string,
  method: Method,
  body: Record<string, unknown>,
) {
  await useFetch(
    `http://localhost:8000/${model}/${action}`,
    {
      server: false,
      method,
      body,
    },
  );
}
