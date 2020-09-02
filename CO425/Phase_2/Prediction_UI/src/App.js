import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import Input from './components/input.js';
import Output from './components/output.js';
import Navbar from './components/navbar.js';
import axios from 'axios';
import serverUrl from './config';

class App extends React.Component {
  state={
    values : {},//{ land_size: "23", beds: "23", baths: "23", house_size: "12", location: "2342" }
    locations:[
      {name:"Angoda",value:0},
      {name:"Athurugiriya",value:1},
      {name:"Avissawella",value:2},
      {name:"Battaramulla",value:3},
      {name:"Boralesgamuwa",value:4},
      {name:"Colombo 10",value:5},
      {name:"Colombo 12",value: 6},
      {name:"Colombo 13",value:7},
      {name:"Colombo 14",value:8},
      {name:"Colombo 15",value:9},
      {name:"Colombo 2",value:10},
      {name:"Colombo 3",value:11},
      {name:"Colombo 4",value:12},
      {name:"Colombo 5",value:13},
      {name:"Colombo 6",value:14},
      {name:"Colombo 7",value:15},
      {name:"Colombo 8",value:16},
      {name:"Colombo 9",value:17},
      {name:"Dehiwala",value:18},
      {name:"Hanwella",value:19},
      {name:"Homagama",value:20},
      {name:"Kaduwela",value:21},
      {name:"Kesbewa",value:22},
      {name:"Kohuwala",value:23},
      {name:"Kolonnawa",value:24},
      {name:"Kottawa",value:25},
      {name:"Kotte",value:26},
      {name:"Maharagama",value:27},
      {name:"Malabe",value:28},
      {name:"Moratuwa",value:29},
      {name:"Mount Lavina",value:30},
      {name:"Nawala",value:31},
      {name:"Nugegoda",value:32},
      {name:"Padukka",value:33},
      {name:"Pannipitiya",value:34},
      {name:"Piliyandala",value:35},
      {name:"Rajagiriya",value:36},
      {name:"Ratmalana",value:37},
      {name:"Talawatugoda",value:38},
      {name:"Wellampitiya",value:39},
    ],
    message :''
  };

  //get locations data from server
  /*
  componentDidMount() {
    console.log('Component did mount!')
    axios.get(serverUrl)
    .then(res => {
      this.setState({locations:res.data})
    })
    .catch(err => { console.log("locations list not get")});
  };*/

  handleSubmit = (values) =>{
    this.setState({values});
    this.handleEvent();
  };

  handleEvent =   () => {
    const values = this.state.values;
    console.log(values);
    axios.get(serverUrl, {params: {
      location: values.location,
      beds: values.beds,
      baths: values.baths,
      house_size: values.house_size,
      land_size: values.land_size
    }})
    .then(res => { 
      this.setState({message:res.data});
      console.log(this.state.message);
    })
    .catch((err) => {
      this.setState({message:"Could not connect with server!"});
    })

  };
  render(){
    return (
      <div className="App">
        <Navbar/>
        <Input onSub={this.handleSubmit} locations={this.state.locations}/>
        <Output message={this.state.message}/>
      </div>
    );
  }
}

export default App;
