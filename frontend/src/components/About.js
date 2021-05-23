import React, { createRef, useState, useCallback } from "react";
import arrow from '../images/backArrow.png'
import { Redirect } from "react-router";
function About(props){
    let [home, goHome] = useState(null)
    const styling = {
        marginLeft:"10vw",
        marginRight:'10vw',
        marginBottom:'5vh',
        fontSize: '28pt'
    }
    if (home != null){
        return <Redirect push to  = "/components/homepage"/>
    }

    return(
        <div style = {{
            background:'linear-gradient(to right, rgba(196,196,196,.9), rgba(234,234,234,.9))',
        }}>
            <p style = {styling}>This artificial intelligence judge was built using the history of every UFC fight in history. Since the UFC does not provide an open source API, The data was collected by creating a scraper to crawl through the stats portion of their website.</p>
            <p style = {styling}>The scraped data was then processed into an organized dataset and further processed into a format that could be processed by the machine learning architecture. The judge model was built using pytorch.</p>
            <p style = {styling}>As is, the model performs with about an 80% accuracy which was found using cross validation of the dataset. This model is built using a minimal amount of features. It is extremely likely with further scraping for more features, the accuracy would increase.</p>
            <div style = {{
                position : 'fixed',
                bottom:'0'
            }}>
                <img src = {arrow} height = '100px' width = '100px'
                onMouseDown={()=>{
                   
                    goHome(true)
                }}></img>
            </div>
        
        </div>
    )

}

export {About}