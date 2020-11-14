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
        externalReferences[i].appendChild(sup);
    }

    // search links are broken
    // maybe add a listener to the url and if url contains "?q" modify the url
}, false);