import React from "react";
import "./HomePage.css"; 
import AImage from "/src/assets/Images/AI.jpg";
import {Link} from "react-router-dom";
const HomePage = () => {

  return (
    <div className="home-page">
      <div className="home-content">
        <h1 className="welcome-text">Welcome to AI Forensic Investigation</h1>
        <p className="about-text">
          AI Forensic Investigation utilizes artificial intelligence and
          advanced technologies to analyze and interpret digital evidence for
          investigative purposes.
        </p>
        <Link to="/audioform">
          <button className="glow-on-hover">Investigate</button>
        </Link>
      </div>
      <img src={AImage} />
    </div>
  );
};

export default HomePage;
