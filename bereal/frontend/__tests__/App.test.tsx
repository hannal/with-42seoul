import React from 'react'
import { render, screen } from '@testing-library/react'

import App from '@/App'

describe('renders app component', () => {
  it('should 회원 가입 in the document', () => {
    render(<App />)
    const element = screen.getByText(/회원 가입/)
    expect(element).toBeInTheDocument()
  })
})
