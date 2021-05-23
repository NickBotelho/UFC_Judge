import React, { createRef, useState, useCallback } from "react";

function Winner(props){

    if (props.win == null){
        return null
    }
    else{
        
        return(
            <div style = {{
                display:'block',
                marginTop:'50px'
            }}>
                <h2
                style = {{
                    color : props.win,
                    textAlign:'center',
                    fontSize:'60pt',
                    textShadow:'1px 1px 1px black'
                }}>{`Winner is: ${props.win.toUpperCase()}`}</h2>
            </div>
        )
    }

}

export {Winner}