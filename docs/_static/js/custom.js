// BIG HACKS BELOW ***DANGER***
// sphinx docs are not very friendly tbh especially when imlpementing markdown
// I apologize for the gruesomeness below but what can you do ¯\_(ツ)_/¯

document.addEventListener('DOMContentLoaded', function() {
    // table of content links work fine, but external links are broken
    // we do some magic here to make external links work

    let sectionMap = [];
    let citationMap = [];
    let citationCounter = 0;
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

        let foundCitation = citationMap.find(c=>c.citation==innerText);
        let newCitation = null;
        if(!foundCitation){
            citationCounter++;
            newCitation = {citation:innerText, number:citationCounter};
            citationMap.push(newCitation);
        }

        let sup = document.createElement("sup");
        let textNode = document.createTextNode(`[${foundCitation?foundCitation.number:newCitation.number}]`);
        sup.appendChild(textNode);
        sup.classList.add('citation');
        externalReferences[i].appendChild(sup);
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