import React, { Component } from 'react'  

export default class Signup extends Component {
    render() {
      return (        
            <div className='mt-5 text-white'>
              <form className='container bg-dark p-5' method='POST'>

                <h2 className='text-center mb-5'>Sign up to NewsVibes</h2>

                <div className="form-outline mb-4">
                    <label className="form-label" name = "username">UserName</label>
                    <input type="text" className="form-control" />
                </div>

                <div className="form-outline mb-4">
                    <label className="form-label" name = "email">Email address</label>
                    <input type="email" className="form-control" />
                </div>

                <div className="form-outline mb-4">
                    <label className="form-label" name = "password">Password</label>
                    <input type="password" className="form-control" />
                </div>

                <div className='d-flex justify-content-center'>
                    <button className="btn btn-primary btn-block mb-4 m-3">
                        <a href="checkmail/" className='text-decoration-none text-white'>Submit</a>
                    </button>
                </div>
                </form>
            </div> 
      )
    }
  } 