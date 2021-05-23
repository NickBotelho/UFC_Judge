import React, { createRef, useState, useCallback } from "react";
//Knockdowns,Strikes,Takedowns,Submission Attempts
function FightInput(props){

    async function sendRequest(fighter1, fighter2){
        const requestSearch = {
            method: "POST",
            headers:  {
                'Content-Type': "application/json; charset=utf-8",
                Accept: "application/json",
                "Cache-Control": "no-cache"
            },
            credentials: "include",
            body: JSON.stringify({
                red: fighter1,
                blue:fighter2
            }),    
        }

        const search_result = await fetch("http://127.0.0.1:5000/predict", requestSearch)
        const data = await search_result.json()
        console.log(data)
        props.setWinner(data['winner'])
    }

    function submit() {
        //console.log(fighter1ref.current.children[0].children[1].value)
        let i = 1 //1 skips the h4 title child
        let fighter1 ={
            name:'red'
        }
        for (i = 1; i < fighter1ref.current.children.length; i++){
            let curr = fighter1ref.current.children[i].children[1].value
            if (i == 1){
                fighter1.kd = curr
            }
            else if (i == 2){
                fighter1.strikes = curr
            }
            else if (i == 3){
                fighter1.td = curr
            }
            else if (i == 4){
                fighter1.sub = curr
            }
        }
        console.log(fighter1)

        i = 1
        let fighter2 ={
            name:'blue'
        }
        for (i = 1; i < fighter2ref.current.children.length; i++){
            let curr = fighter2ref.current.children[i].children[1].value
            if (i == 1){
                fighter2.kd = curr
            }
            else if (i == 2){
                fighter2.strikes = curr
            }
            else if (i == 3){
                fighter2.td = curr
            }
            else if (i == 4){
                fighter2.sub = curr
            }
        }
        console.log(fighter2)
        sendRequest(fighter1, fighter2)
    }
    let fighter1ref = createRef()
    let fighter2ref = createRef()
    return (
        <div>
            <div style = {{
                display:'flex',
                flexDirection:'row',
                justifyContent:'space-evenly',

            }}>
                <div ref = {fighter1ref}>
                    <h4 style = {{
                        // textAlign:'center',
                        color:'red',
                        fontSize:'25pt',
                        textShadow:'1px 1px 1px black'
                    }}>RED</h4>
                    <div>
                    <label style={{
                        display:"block"
                    }}>Knockdowns</label>
                    <input
                            type = 'text'
                            // ref = {kd1}
                            id = 'kd1'
                
                            placeholder = '0'
                            style = {{
                                display:"block",
                                cursor:"pointer"
                            }}
                            // onChange = {updateKD}   
                        ></input>  
                </div>
                    <div>
                    <label style={{
                        display:"block"
                    }}>Strikes</label>
                    <input
                            type = 'text'
                            // ref = {kd1}
                            id = 'strikes1'
                
                            placeholder = '0'
                            
                            style = {{
                                display:"block",
                                cursor:"pointer"
                            }}
                            // onChange = {updateKD}   
                        ></input>  
                </div>
                    <div>
                    <label style={{
                        display:"block"
                    }}>Takedowns</label>
                    <input
                            type = 'text'
                            // ref = {kd1}
                            id = 'td1'
                
                            placeholder = '0'
                             
                            style = {{
                                display:"block",
                                cursor:"pointer"
                            }}
                            // onChange = {updateKD}   
                        ></input>  
                </div>
                    <div>
                    <label style={{
                        display:"block"
                    }}>Submission Attempts</label>
                    <input
                            type = 'text'
                            // ref = {kd1}
                            id = 'sub1'
                
                            placeholder = '0'
                             
                            style = {{
                                display:"block",
                                cursor:"pointer"
                            }}
                            // onChange = {updateKD}   
                        ></input>  
                </div>
                </div>


                <div ref = {fighter2ref}>

                    <h4 style = {{
                        // textAlign:'center',
                        color:'blue',
                        fontSize:'25pt',
                        textShadow:'1px 1px 1px black'
                    }}>BLUE</h4>
                    <div>
                        <label style={{
                            display:"block"
                        }}>Knockdowns</label>
                        <input
                                type = 'text'
                                placeholder = '0'
                                 
                                style = {{
                                    display:"block",
                                    cursor:"pointer"
                                }} 
                            ></input>  
                    </div>
                    <div>
                        <label style={{
                            display:"block"
                        }}>Strikes</label>
                        <input
                                type = 'text'
                                placeholder = '0'
                                 
                                style = {{
                                    display:"block",
                                    cursor:"pointer"
                                }}  
                            ></input>  
                    </div>
                    <div>
                        <label style={{
                            display:"block"
                        }}>Takedowns</label>
                        <input
                                type = 'text'
                                placeholder = '0'
                                 
                                style = {{
                                    display:"block",
                                    cursor:"pointer"
                                }} 
                            ></input>  
                    </div>
                    <div>
                    <label style={{
                        display:"block"
                    }}>Submission Attempts</label>
                    <input
                            type = 'text'
                            placeholder = '0'
                             
                            style = {{
                                display:"block",
                                cursor:"pointer"
                            }}  
                        ></input>  
                </div>
                </div>
            </div>

            <div style = {{

                marginTop:'75px',
                display:'flex',
                justifyContent:'center',
            }}>
                <button style = {{
                    height:'40px',
                    width:'250px',
                    cursor:'pointer',
                    border:"2pt solid black",
                    fontFamily:'Kanit'
                }}
                onClick = {submit}>Submit</button>
            </div>






            
       
                    
        </div>

    )

}

export {FightInput}