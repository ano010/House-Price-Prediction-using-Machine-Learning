import 'bootstrap/dist/css/bootstrap.css';
import React, { Component } from 'react';

class Navbar extends Component{
    render() {
        return (
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark d-flex">
                <a className="navbar-brand" href="#">
                    House Price Estimater
                </a>
            </nav>
           
        );
      }
}
export default Navbar;