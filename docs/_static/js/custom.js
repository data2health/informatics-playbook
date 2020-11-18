// BIG HACKS BELOW ***DANGER***
// sphinx docs are not very friendly tbh especially when imlpementing markdown
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