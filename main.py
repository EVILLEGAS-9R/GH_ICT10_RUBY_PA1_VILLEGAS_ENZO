from pyscript import display

basketball = {'Enzo', 'Koby', 'Seth'}
volleyball = {'Koby', 'Tarcisius', 'Seth'}


display(basketball | volleyball, target='output')


display(basketball & volleyball, target='output')


display(basketball - volleyball, target='output')


display(volleyball - basketball, target='output')


display(basketball ^ volleyball, target='output')
