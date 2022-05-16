import React, { Suspense } from 'react'
import { BrowserRouter } from 'react-router-dom'

import SignUp from './SignUp'
import { useSignUp } from './useSignUp'

function App() {
  const [payload, setPayload] = React.useState(null)
  const signup = useSignUp(payload)

  const onSignUp = (data: any) => {
    setPayload(data)
  }

  return (
    <Suspense fallback={<div>loading...</div>}>
      <BrowserRouter>
        <SignUp onSubmit={onSignUp} />
      </BrowserRouter>
    </Suspense>
  )
}

export default App
