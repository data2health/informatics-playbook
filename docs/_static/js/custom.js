// BIG HACKS BELOW ***DANGER***
// sphinx docs are not very friendly tbh especially when implementing markdown
// I apologize for the gruesomeness below but what can you do ¯\_(ツ)_/¯

document.addEventListener('DOMContentLoaded', function() {
    // table of content links work fine, but external links are broken
    // we do some magic here to make external links work

    let sectionMap = [];
    let references = document.getElementsByClassName('reference internal');
    let externalReferences = document.getElementsByClassName('reference external');

    for(let i = 0; i < references.length; i++){
       const element = references[i];
       sectionMap.push({href:element.href, text:element.innerText.toLowerCase()})
    }

    for(let i = 0; i < externalReferences.length; i++){
        let innerText = externalReferences[i].innerText.toLowerCase()
        let internalReference = sectionMap.find(section=>section.text == innerText);
        if(internalReference){
            externalReferences[i].href = internalReference.href;
        }

        // wrap all citations with <sup> elements
        if(externalReferences[i].hash && externalReferences[i].hash.match(/^#kix/i)){
            let sup = document.createElement("sup");
            externalReferences[i].insertAdjacentElement('beforebegin', sup);
            sup.insertAdjacentElement('afterbegin', externalReferences[i]);
        }
    }

    // footnotes in text are in a different order than the one google docs api provides us
    // so the below unfortunately does not work, so we have to do some magic... again

    let citations = [].slice.call(document.querySelectorAll('a')).filter(function(el){
       return el.hash.match(/^#kix/i);
    });

    // populating the footnoteMap array based on the citations found above
    let footnoteMap = [];
    for(let i=0; i<citations.length; i++){
        let reference = citations[i];
        footnoteMap.push({index:i+1, id:reference.hash});
    }


    // Then we use the footnoteMap array to add footnote indexing and enable linking
    let referenceElements = document.getElementById('references');
    if(referenceElements){
        for(let i=0; i<referenceElements.children.length; i++){
            // First element will be the header title which we don't need
            if(i==0) {
                continue;
            }
            let reference = referenceElements.children[i];
            // get all anchor elements below the reference that specify the reference id
            let referenceAnchorNodes = [].slice.call(reference.
            querySelectorAll('a')).filter(function(el){
               return el.hash.match(/^#kix/i);
            });
            const id = referenceAnchorNodes[0].hash;

            let foundReference = footnoteMap.find(f=>f.id==id);
            if(foundReference){
                let sup = document.createElement("sup");
                sup.id = foundReference.id.substring(1);
                let textNode = document.createTextNode(`${foundReference.index} `);
                sup.appendChild(textNode);
                reference.prepend(sup);
            }
        }
    }

    // since sphinx's recommonmark does not handle strikethroughs, we handle it manually
    // check all 'p' elements which contain ~~****~~ and convert them to <strike>
    [].slice.call(document.querySelectorAll('p')).forEach(function(el){
        let match = el.innerText.match(/[~~].*[~~]/)
        if (match){
            let before = document.createElement("span");
            let after = document.createElement("span");
            let strikethrough = document.createElement("strike")
            let beforeTextNode = document.createTextNode(match.input.slice(0,match.index));
            let afterTextNode = document.createTextNode(match.input.slice(match.index + match[0].length));
            let strikethroughTextNode = document.createTextNode(match[0].split('~').join(''));
            before.appendChild(beforeTextNode);
            after.appendChild(afterTextNode);
            strikethrough.appendChild(strikethroughTextNode);

            el.insertAdjacentElement('beforebegin',before);
            el.insertAdjacentElement('beforebegin',strikethrough);
            el.insertAdjacentElement('afterend',after);

            el.parentNode.removeChild(el);
        }
    });

    // Find all youtube links and replace them with embeds
    [].slice.call(document.querySelectorAll('a')).forEach(function(el){
        // first check if its a youtube link
        if(el.href.match('https://(www.)?youtube|youtu\.be')){
            // then find the youtube vid id
            let regExp = /.*(?:youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=)([^#\&\?]*).*/;
            let match = el.href.match(regExp);
            if(match){
                let id = (match&&match[1].length==11)? match[1] : false;
                let src = `https://www.youtube.com/embed/${id}?autoplay=1&mute=1"`;
                let ifrm = document.createElement("iframe");
                ifrm.setAttribute("src", src);
                ifrm.style.width = "640px";
                ifrm.style.height = "480px";
                el.insertAdjacentElement('beforebegin', ifrm);
                el.parentNode.removeChild(el);
                //document.body.appendChild(ifrm);
            }
        }
    });

    // sphinx's recommonmark does not like consecutive italics and leaves '*' sometimes hanging in the html
    // we use this to clean up most of the mess
    [].slice.call(document.querySelectorAll('em')).forEach(function(el){
        el.innerHTML = el.innerHTML.split('*').join('')
    });

    // Temporary hack for broken search links
    // Some search result links look like this "chapters/chapter_6undefined?highlight=harmonization"
    // It seems that the theme parses the page extension to "undefined" instead of ".html"
    // We check in each anchor link if this is the case and replace the href
    if(window.location.href.includes('search.html')){
        // apparently the theme does some modification after the dom has been loaded
        let tries = 0;
        let interval = setInterval(function () {
            if(tries>5){
                clearInterval(interval)
            }
            tries++;
            let anchors = document.getElementsByTagName('a');
            for (let i = 0; i < anchors.length; i++) {
                if (anchors[i].href.includes('undefined')) {
                    anchors[i].href = anchors[i].href.replace('undefined', '.html');
                }
            }
        }, 1000)
    }

    // search links are broken
    // maybe add a listener to the url and if url contains "?q" modify the url
}, false);