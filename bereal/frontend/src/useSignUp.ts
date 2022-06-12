import useSWR from 'swr'
import { Payload, SignUpSuccess } from './SignUp'

export const fetcher = async (url: string, payload: Payload) => {
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  })
  return await res.json()
}

export const useSignUp = (payload?: Payload) => {
  const result = useSWR<Payload>(payload ? '/signup/' : null, fetcher)

  const data =
    !result.isValidating && !!result.data
      ? ({ username: payload?.username } as SignUpSuccess)
      : undefined

  return {
    data,
    isValidating: result.isValidating,
    error: result.error,
    mutate: result.mutate,
  }
}
