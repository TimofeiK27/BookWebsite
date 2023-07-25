
fetch('/posts')
   .then(response => response.json())
   .then(text => {

        console.log(text)
        posts = document.querySelector('#posts');
        totalPosts = 6;

        text.forEach(function(text){       
            post = document.createElement('div');
            
            post.style.width='800px';
            post.style.height='200px';
            post.style.margin='10px auto 10px auto';
            post.style.padding='10px 0px 0px 40px';
            post.style.border='lightgrey 3px solid';
            post.id = text.id;

            title = document.createElement('h3');
            title.innerHTML = text.title;

            description = document.createElement('h4');
            description.innerHTML = text.description;

            del = document.createElement('submit');
           del.style.width="120px";
           del.style.height="20px";
           del.style.margin="40px 0px 0px 0px";
            del.innerHTML = "DELETE";
            del.style.background = "pink";
            del.id = `${text.id}del`;

            reqbtn = document.createElement('submit');
            reqbtn.style.width="120px";
            reqbtn.style.height="20px";
            reqbtn.style.margin="0px 0px 0px 0px";
            reqbtn.innerHTML = "Request Book";
            reqbtn.style.background = "lightblue";
            reqbtn.id = `${text.id}req;`;
 
            post.append(title);
            post.append(description);
            post.append(del);
            post.append(req);
            posts.append(post);

            document.getElementById(`${text.id}del`).addEventListener("click", (delPost)=> {
                document.getElementById(text.id).remove();
                console.log(1);
                fetch('/posts', {
                    method: 'POST',
                    data: {csrfmiddlewaretoken: "{{ csrf_token }}", state:"inactive"},
                    body: JSON.stringify({
                       id : text.id
                   })} 
                ) 
                
            })
        })
});