Cypress.Commands.add("cookies", () => { 
    cy.get('#sp-cc-accept').click()
}); 

Cypress.Commands.add("searchText", (searchText) => { 
    cy.get('#twotabsearchtextbox').type(searchText)
    cy.get('#nav-search-submit-button').click()

}); 