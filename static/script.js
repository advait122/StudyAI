let currentSubject = "";

loadSubjects();

async function uploadPDF(){

    const file = document.getElementById("pdfFile").files[0];

    if(!file){
        alert("Choose a PDF");
        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    await fetch("/upload",{
        method:"POST",
        body:formData
    });

    loadSubjects();
}

async function loadSubjects(){

    const response = await fetch("/subjects");

    const subjects = await response.json();

    const div = document.getElementById("subjects");

    div.innerHTML="";

    subjects.forEach(subject=>{

        const box=document.createElement("div");

        box.className="subject";

        box.innerText=subject;

        box.onclick=()=>openSubject(subject);

        div.appendChild(box);

    });

}

function openSubject(subject){

    currentSubject=subject;

    document.getElementById("chatSection").style.display="block";

    document.getElementById("subjectTitle").innerText=subject;

    document.getElementById("chatBox").innerHTML="";
}

async function askQuestion(){

    const question=document.getElementById("question").value;

    if(question==="") return;

    const chat=document.getElementById("chatBox");

    chat.innerHTML+=`
        <div class="user">
            <b>You:</b><br>${question}
        </div>
    `;

    const response=await fetch(`/ask?question=${encodeURIComponent(question)}&subject=${encodeURIComponent(currentSubject)}`,{
        method:"POST"
    });

    const data=await response.json();

    chat.innerHTML+=`
        <div class="bot">
            <b>SmartStudyAI:</b><br>${data.answer}
        </div>
    `;

    document.getElementById("question").value="";

    chat.scrollTop=chat.scrollHeight;

}