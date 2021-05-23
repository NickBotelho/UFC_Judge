import React from "react";
import { Route, BrowserRouter as Router, Switch } from "react-router-dom";
import {Homepage} from './components/Homepage.js'
import {About} from './components/About.js'
function Routing(props) {
    const navRoutes={
        homepage:"/components/homepage",
        about:'/components/about'
    }
    return (
        <div
            style={{
                display: "flex",
                flexDirection: "column",
                marginBottom: "80px",
            }}
        >
            <Router>
                <div style={{ width: "100%" }}>
                    <Switch>
                        
                        <Route exact path={navRoutes.about} component={About}/>
                        <Route exact path ={navRoutes.homepage} component={Homepage}/>
                        <Route component={Homepage} />             
                    </Switch>
                </div>
            </Router>
        </div>
    );
}

export { Routing };