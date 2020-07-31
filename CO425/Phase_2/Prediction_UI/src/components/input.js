
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import 'font-awesome/css/font-awesome.min.css';
import './components.css'
import React, { Component } from 'react';
import { useForm ,Controller} from "react-hook-form";
import CoordinateInput from 'react-coordinate-input';
export default function Input(props) {
      const { register, handleSubmit, control, watch, errors } = useForm();
      const onSubmit = data =>{
        // console.log(data);
        props.onSub(data);
      };
        return (
          <div className="Input  row align-items-center">
            <div className="col"></div>
            <div className="col-12 col-xs-10 col-sm-8 col-md-8 col-lg-6 mt-4">  
              <form className="card m-4 " onSubmit={handleSubmit(onSubmit)} >
                {/* <div className="card-header"> Input </div> */}
                <div className="card-body">
                    <div className="form-group row" >
                      <label htmlFor="land_size" className="col-sm-4 col-form-label " >Land size (perch)</label>
                      <div className="col-sm-8">
                      <div className="input-group mb-3">
                        <input ref={register({ required: true, min:0 })} type="number" step="0.001" min="0" className="form-control input-field" name="land_size" placeholder="Land size"/>
                        <span>{errors.land_size && <i className="fa fa-exclamation-circle Icon"></i>}</span>
                      </div>
                      </div>
                    </div>
      
                    <div className="form-group row">
                      <label htmlFor="beds" className="col-sm-4 col-form-label">No.of Beds</label>
                      <div className="col-sm-8">
                      <div className="input-group mb-3">
                       <input ref={register({ required: true, min:0 })} type="number" min="0" className="form-control" name="beds" placeholder="Number of beds"/>
                        <span>{errors.beds && <i className="fa fa-exclamation-circle Icon"></i>}</span>
                      </div>
                      </div>
                    </div>
      
                    <div className="form-group row">
                      <label htmlFor="baths" className="col-sm-4 col-form-label">No.of Bathrooms</label>
                      <div className="col-sm-8">
                      <div className="input-group mb-3">
                       <input ref={register({ required: true, min:0 })} type="number" min="0" className="form-control" name="baths" placeholder="Number of bathrooms"/>
                        <span>{errors.baths && <i className="fa fa-exclamation-circle Icon"></i>}</span>
                      </div>
                      </div>
                    </div>
      
                    <div className="form-group row" >
                      <label htmlFor="house_size" className="col-sm-4 col-form-label " >House size (sqft)</label>
                      <div className="col-sm-8">
                      <div className="input-group mb-3">
                       <input ref={register({ required: true, min:0 })} type="number" step="0.001" min="0" className="form-control " name="house_size" placeholder="House size"/>
                        <span>{errors.house_size && <i className="fa fa-exclamation-circle Icon"></i>}</span>
                      </div>
                      </div>
                    </div>
      
                    <div className="form-group row" >
                      <label htmlFor="location" className="col-sm-4 col-form-label " >Location</label>
                      <div className="col-sm-8">
                      <div className="input-group mb-3">
                        <select className="custom-select custom-select-sm" ref={register({ required: true})} name="location">
                            <option defaultValue value=''>Open this select menu</option>
                            {props.locations.map((location) =>  <option value={location.value} key={location.value}>{location.name}</option>)}
                        </select>
                      <span>{errors.location && <i className="fa fa-exclamation-circle Icon"></i>}</span>
                      </div>
                      </div>
                    </div>
                    
                    <div className="form-group row">
                      <div className="col-sm-10">
                        <button type="submit" className="btn btn-primary" >Estimate</button>
                      </div>
                    </div>
                  </div>
              </form>
              </div>    
            
            <div className="col">
            
            </div>
          </div>
           
        );
      
    
  }
