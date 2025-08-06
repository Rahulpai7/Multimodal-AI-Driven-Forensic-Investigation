import React from "react";
import "./Navbar.css"; 
import { Link } from "react-router-dom";
import Logo from "/src/assets/Images/logo.png";

const Navbar = () => {

  return (
    <nav className="navbar">
        <img src={Logo} alt="Logo" />
      <ul className="navbar-links">
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/dashboard">Dashboard</Link>
        </li>
        <li>
          <Link to="/audioform">Investigate</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
