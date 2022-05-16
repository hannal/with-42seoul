module.exports = {
  preset: 'ts-jest/presets/js-with-ts',
  testEnvironment: 'jest-environment-jsdom',
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx'],
  globals: {
    'ts-jest': {
      diagnostics: true,
      isolatedModules: true,
    },
  },
  setupFiles: ['./setupTests.ts', 'jest-localstorage-mock'],
  setupFilesAfterEnv: ['./setupTestsAfterEnv.ts'],
  testMatch: ['<rootDir>/**/__tests__/**/*.[jt]s?(x)'],
  modulePathIgnorePatterns: [
    '<rootDir>/build/',
    '<rootDir>/__tests__/@helpers/',
  ],
  transformIgnorePatterns: [
    '<rootDir>/node_modules/(?!antd|@ant-design|rc-.+?|@babel/runtime).+(js|jsx)$',
  ],
  moduleNameMapper: {
    '^@\\/(.*)$': '<rootDir>/src/$1',
    '^@@\\/(.*)$': '<rootDir>/__tests__/$1',
    '^@@@\\/(.*)$': '<rootDir>/__mocks__/$1',
    '.+\\.(css|styl|less|sass|scss|png|jpg|ttf|woff|woff2)$':
      '<rootDir>/__mocks__/styleMock.js',
  },
  transform: {
    '.+\\.svg$': '<rootDir>/__mocks__/svgMock.js',
  },
}
