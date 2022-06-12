import useSWR from 'swr'
import { Payload, SignUpSuccess } from './SignUp'

export const useSignUp = (payload?: Payload) => {
  const result = useSWR<Payload>(payload ? '/signup/' : null, async () => {
    const data = {
      ...payload,
    }
    return data as Payload
  })

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
