import React from "react";
import { render, screen, fireEvent } from "@testing-library/react";

import SignUp, { Payload } from "@/SignUp";

describe("renders SignUp component", () => {
  const mockOnSubmit = jest.fn();

  it("should 회원 가입 in the document", () => {
    render(<SignUp onSubmit={mockOnSubmit} />);
    expect(screen.getByText(/회원 가입/)).toBeInTheDocument();
    expect(screen.getByText(/아이디/)).toBeInTheDocument();
    expect(screen.getByText(/비번/)).toBeInTheDocument();
    expect(screen.getByText(/회원가입하기/)).toBeInTheDocument();
  });

  it("유효한 id/pw를 넣으면 회원가입 요청을 할 수 있다.", () => {
    render(<SignUp onSubmit={mockOnSubmit} />);
    const payload: Payload = {
      username: "42seoul",
      password: "seoul",
    };
    fireEvent.change(screen.getByTestId("input-username"), {
      target: { value: payload.username },
    });
    fireEvent.change(screen.getByTestId("input-passwd"), {
      target: { value: payload.password },
    });
    fireEvent.click(screen.getByTestId("btn-submit"));

    expect(mockOnSubmit).toBeCalledWith(payload);
  });
});
