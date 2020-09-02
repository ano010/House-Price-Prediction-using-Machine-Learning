import 'bootstrap/dist/css/bootstrap.css';
import React, { Component } from 'react';

class Output extends Component{
    render() {
        return (
          <div className="Input  row align-items-center">
            <div className="col"></div>

            <div className="col-12 col-xs-10 col-sm-8 col-md-8 col-lg-6 w-100 ">  
                <div className="card m-4">
                    {/* <div className="card-header">
                        Output
                    </div> */}
                    <div className="card-body">
                        {/* <div className="row">
                          <div className="col">
                            <h4>Estimated house price:</h4>
                          </div>
                        </div> */}

                        <div className="row justify-content-center">
                        <div className="col">
                            <div id="message">
                              {'Rs. '}
                              {Math.trunc(this.props.message)}
                            </div>
                          </div>
                        </div>
                    </div>
                </div>
            </div>    
            
            <div className="col"></div>
          </div>
           
        );
      }
}
export default Output;