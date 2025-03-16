function setup() {
    createCanvas(1000, 1000);
    background(0);
    noStroke();
  }


function draw() {

        // 무지개! 같은 선을 만듭니다!
    // 우선 무지개 색을 정의합니다.
    red = color(238, 30, 50);
    orange = color(241, 99, 35);
    yellow = color(254, 241, 1);
    green = color(34, 169, 81);
    indigo = color(33, 168, 198);
    violet = color(114, 92, 145);

    // 6번 반복하며 y좌표를 10씩 증가시키고, x좌표도 6씩 증가시킵니다.
    for (let i = 0; i < 6; i++) {
        if (i == 0) {
            fill(red);
        } else if (i == 1) {
            fill(orange);
        } else if (i == 2) {
            fill(yellow);
        } else if (i == 3) {
            fill(green);
        } else if (i == 4) {
            fill(indigo);
        } else if (i == 5) {
            fill(violet);
        }
        beginShape();
        vertex(1000, 486+(10*i));
        vertex(565+(6*i), 350+(10*i));
        vertex(575+(6*i), 365+(10*i));
        if (i == 5) { //그냥 하면 끝이 다 안 맞아서 이렇게 처리했습니다.
            vertex(1000, 495+(10*i));
        }
        else {
            vertex(1000, 486+(10*(i+1)));
        }
        endShape(CLOSE);
    }
   
    let n = 255;
    let lx1 = 500;
    let ly1 = 230;
    let lx2 = 320;
    let ly2 = 540;
    let lx3 = 680;
    let ly3 = 540;

    let fx1 = 500;
    let fy1 = 270;
    let fx2 = 360;
    let fy2 = 520;
    let fx3 = 640;
    let fy3 = 520;

   // 삼각형에 색을 흰색으로 채우고, 검은색 삼각형이 가운데에 위치하도록 그래디언트를 설정합니다. 마참내!
    fill(255, 255, 255);
    triangle(lx1, ly1, lx2, ly2, lx3, ly3);

    fill(0, 0, 0);
    triangle(fx1, fy1, fx2, fy2, fx3, fy3);

    for (let i = 0; i < n; i++) {
        let x1 = lx1-((lx1-fx1)/n)*i;
        let y1 = ly1-((ly1-fy1)/n)*i;
        let x2 = lx2-((lx2-fx2)/n)*i;
        let y2 = ly2-((ly2-fy2)/n)*i;
        let x3 = lx3-((lx3-fx3)/n)*i;
        let y3 = ly3-((ly3-fy3)/n)*i;
        fill(255-i, 255-i, 255-i, 255);
        triangle(x1, y1, x2, y2, x3, y3);
 
    }

    // 삼각형 만들기 위한 재료?
    let ix1 = 390;
    let iy1 = 385;
    let ix2 = 560;
    let iy2 = 335;
    let ix3 = 605;
    let iy3 = 410;


    // 우선 ix1과 ix2 사이의 2분의 1 지점을 계산합니다.
    let ix1_2 = 500;
    let iy1_2 = iy1 + (iy2 - iy1) / 2;

    // ix1과 ix3 사이의 2분의 1 지점을 계산합니다.
    let ix1_3 = 500;
    let iy1_3 = iy1 + (iy3 - iy1) / 2;

    // 하얀 선을 그립니다.
    fill(255, 255, 255);
    beginShape();
    vertex(0, 486);
    vertex(417, 374);
    vertex(413, 381);
    vertex(0, 495);
    endShape(CLOSE);

    // 하얀 선의 x가 각각 417, 413인 좌표부터 ix1_2, iy1_2, ix1_3, iy1_3까지 그립니다. 젭알!
    for (let i = 0; i < n; i++) {
        let x1 = ix1_2-((ix1_2-417)/n)*i;
        let y1 = iy1_2-((iy1_2-374)/n)*i;
        let x2 = ix1_3-((ix1_3-413)/n)*i;
        let y2 = iy1_3-((iy1_3-381)/n)*i;
        fill(0+i, 0+i, 0+i, 255);
        beginShape();
        vertex(x1, y1);
        vertex(x2, y2);
        vertex(417, 374);
        vertex(413, 381);
        endShape(CLOSE);
    }



}