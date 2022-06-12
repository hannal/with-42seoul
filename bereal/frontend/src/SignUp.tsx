import React, { useRef, FormEvent } from 'react'

export interface Payload {
  username: string
  password: string
}

export interface SignUpSuccess {
  username: string
}

interface PropType {
  onSubmit: (data: Payload) => void
}

const SignUp: React.FC<PropType> = ({ onSubmit }) => {
  const payload = useRef<Payload>({
    username: '',
    password: '',
  })

  const _onSubmit = (e: FormEvent) => {
    e.preventDefault()
    onSubmit(payload.current)
  }

  return (
    <div>
      <h1>회원 가입</h1>

      <form onSubmit={_onSubmit}>
        <div>
          <label htmlFor="id-username">아이디</label>
          <input
            data-testid="input-username"
            id="id-username"
            type="text"
            name="username"
            onChange={(e) => (payload.current.username = e.target.value)}
          />
        </div>

        <div>
          <label htmlFor="id-password">비번</label>
          <input
            data-testid="input-passwd"
            id="id-password"
            type="password"
            name="password"
            onChange={(e) => (payload.current.password = e.target.value)}
          />
        </div>

        <div>
          <button data-testid="btn-submit" type="submit" onClick={_onSubmit}>
            회원가입하기
          </button>
        </div>
      </form>
    </div>
  )
}

export default SignUp
