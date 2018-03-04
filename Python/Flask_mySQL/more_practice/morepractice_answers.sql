#four tables: clients sites, billing, leads


# GOAL: find all clients (first and last name) billing amounts and charged date
SELECT clients.first_name, clients.last_name, billing.amount, billing.charged_datetime
FROM clients
JOIN billing on clients.id = billing.clients_id; 

# GOAL: list all the domain names and leads (first and last name) for each site
SELECT sites.domain_name, leads.first_name, leads.last_name
FROM sites
JOIN leads ON sites.id = leads.sites_id; 

# GOAL: get the names of clients, their domain names and the first names of all the leads generated from those sites
SELECT clients.first_name, clients.last_name, sites.domain_name, leads.first_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads on sites.id = leads.sites_id