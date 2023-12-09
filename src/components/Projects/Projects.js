import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import ProjectCard from "./ProjectCards";
import Particle from "../Particle";
import leaf from "../../Assets/Projects/leaf.png";
import emotion from "../../Assets/Projects/emotion.png";
import editor from "../../Assets/Projects/codeEditor.png";
import chatify from "../../Assets/Projects/chatify.png";
import suicide from "../../Assets/Projects/suicide.png";
import bitsOfCode from "../../Assets/Projects/blog.png";

function Projects() {
  return (
    <Container fluid className="project-section">
      <Particle />
      <Container>
        <h1 className="project-heading">
          My Recent <strong className="purple">Works </strong>
        </h1>
        <p style={{ color: "white" }}>
          Here are a few projects I've worked on recently.
        </p>
        <Row style={{ justifyContent: "center", paddingBottom: "10px" }}>
          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={chatify}
              isBlog={false}
              title="SMM Panel"
              description="Automated Facebook [profile followrs ,page like & follow ,comments on post , group joining ,and reaction]  tools Working system : automatic Work on target   using stored Facebook pages in files.Working speed super high"
              ghLink="https://github.com/Shuvo-BBHH"
              demoLink="https://fb.watch/oPItXGNtyn/"
            />
          </Col>

          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={bitsOfCode}
              isBlog={false}
              title="ON 2F On Facebook"
              description="This is a symple project for on 2F on facebook acount use python..Full automatic and so fast"
              ghLink="https://github.com/Shuvo-BBHH/F_2F"
              demoLink="https://fb.watch/oPJmiL5FeZ"
            />
          </Col>

          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={editor}
              isBlog={false}
              title="Simple messages Boo"
              description="Simple messages Boot using only python reply new messages or messages request 24 houre actives . This a Boot connect wi Ai . So i can reply any question . Host in any site fro running this boot"
              //ghLink="https://github.com/soumyajit4419/Editor.io"
              demoLink="https://fb.watch/oPJKF7vnpU/"              
            />
          </Col>

          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={leaf}
              isBlog={false}
              title="Online Chat Application"
              description="Online Chat Application.Full secure chat transfer.Only Python.server and clint"
              //ghLink="https://github.com/soumyajit4419/Plant_AI"
              demoLink="https://fb.watch/oPKkADdPBr/"
            />
          </Col>

          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={suicide}
              isBlog={false}
              title="Flask Application"
              description="YouTube Video Downloader Web App with Python and Flask also added HTML and CSS JS"
              //ghLink="https://github.com/soumyajit4419/AI_For_Social_Good"
              demoLink="https://fb.watch/oPKAoTJoXQ/" //<--------Please include a demo link here
            />
          </Col>

          <Col md={4} className="project-card">
            <ProjectCard
              imgPath={emotion}
              isBlog={false}
              title="Face Recognition and Emotion Detection"
              description="Automatics voting or polling supper fast ..
              1 munite 1k+ voting . This only for busness parpase"
              //ghLink="https://github.com/soumyajit4419/Face_And_Emotion_Detection"
              demoLink="https://fb.watch/oPKI0t0IMq/"//<--------Please include a demo link here 
            />
          </Col>
        </Row>
      </Container>
    </Container>
  );
}

export default Projects;
