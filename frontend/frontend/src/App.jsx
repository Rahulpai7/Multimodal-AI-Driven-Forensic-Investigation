import React, { useState } from "react";
import './App.css'
import Navbar from "./components/Navbar/Navbar";
import HomePage from "./components/HomePage/HomePage";
import ProblemStatement from "./components/Problem/Problem";
import Solution from "./components/Solution/Solution";
import AudioForm from "./components/AudioForm/AudioForm";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Home from "./components/Home";
import Dashboard from "./components/DashBoard/DashBoard/Dashboard";


function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: (
        <>
          <Navbar />
          <Home />
        </>
      ),
    },
    {
      path: "/dashboard",
      element: (
        <>
          <Navbar />
          <Dashboard />
        </>
      ),
    },
    {
      path: "/audioform",
      element: (
        <>
          <Navbar />
          <AudioForm />
        </>
      ),
    },
  ]);
   return (
     <div className="App">
      <RouterProvider router={router}/>
     </div>
   );
}

export default App
