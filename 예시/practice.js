function setup(){
    createCanvas(600,600)
    background(0)
}

function draw(){
    noStroke()
    fill(255,160,180)
    for(let i=0;i<12;i++)
        rect(50*i,50*i,50,50)
    noFill()
    stroke(255)
    strokeWeight(4)
    for(let i=0;i<12;i++)
        ellipse(25+50*i,height-50*i-25,50,50)

}