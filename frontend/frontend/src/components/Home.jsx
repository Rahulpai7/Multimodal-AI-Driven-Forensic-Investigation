import React from 'react'
import HomePage from './HomePage/HomePage'
import ProblemStatement from './Problem/Problem'
import Solution from './Solution/Solution'

const Home = () => {
  return (
    <div>
        <HomePage/>
        <ProblemStatement/>
        <Solution/>
    </div>
  )
}

export default Home