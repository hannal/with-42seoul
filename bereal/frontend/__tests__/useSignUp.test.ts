import { renderHook, act } from '@testing-library/react-hooks'

import { Payload } from '@/SignUp'
import { useSignUp } from '@/useSignUp'

describe('useSignUp hook', () => {
  it('회원가입 payload가 falsy하면 회원가입 API를 호출하지 않는다.', () => {
    const { result } = renderHook(() => useSignUp())
    expect(result.current.data).toBeFalsy()
  })

  it('회원가입 payload가 유효하면 회원가입 API를 호출하고, 결과를 응답 받는다.', async () => {
    let payload: Payload = {
      username: '42seoul',
      password: 'seoul',
    }

    const hook = renderHook(() => useSignUp(payload))
    await hook.waitFor(() => hook.result.current.data !== undefined)
    expect(hook.result.current.data?.username).toEqual(payload.username)

    payload = {
      ...payload,
      username: 'innoaca',
    }
    await act(async () => {
      hook.result.current.mutate(payload)
    })
    await hook.waitFor(() => hook.result.current.data !== undefined)
    expect(hook.result.current.data?.username).toEqual(payload.username)
  })
})
