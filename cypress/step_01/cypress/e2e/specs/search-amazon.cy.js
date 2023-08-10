describe('Verify Amazon search page', () => {

    it('Verify load page', () => {
        cy.visit('/')
        cy.cookies();
        cy.get('#nav-logo-sprites').should('be.visible');
    })

    it('Search product', () => {
        cy.visit('/')
        cy.cookies();
        cy.searchText('Gibson SG');
        cy.contains('Epiphone SG Standard Ebony')
    })
    
    
})


