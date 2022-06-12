import { renderHook, act } from '@testing-library/react-hooks'

import { Payload } from '@/SignUp'
import * as signUpHook from '@/useSignUp'

describe('useSignUp hook', () => {
  it('회원가입 payload가 falsy하면 회원가입 API를 호출하지 않는다.', () => {
    const { result } = renderHook(() => signUpHook.useSignUp())
    expect(result.current.data).toBeFalsy()
  })

  it('회원가입 payload가 유효하면 회원가입 API를 호출하고, 결과를 응답 받는다.', async () => {
    let payload: Payload = {
      username: '42seoul',
      password: 'seoul',
    }
    const mockFetcher = jest.spyOn(signUpHook, 'fetcher').mockResolvedValue({
      username: payload.username,
    })

    const hook = renderHook(() => signUpHook.useSignUp(payload))
    await hook.waitFor(() => hook.result.current.data !== undefined)
    expect(hook.result.current.data?.username).toEqual(payload.username)
    expect(mockFetcher).toHaveBeenCalledWith('/signup/')

    payload = {
      ...payload,
      username: 'innoaca',
    }
    await act(async () => {
      hook.result.current.mutate(payload)
    })
    await hook.waitFor(() => hook.result.current.data !== undefined)
    expect(hook.result.current.data?.username).toEqual(payload.username)
    expect(mockFetcher).toHaveBeenCalledWith('/signup/')
  })
})
