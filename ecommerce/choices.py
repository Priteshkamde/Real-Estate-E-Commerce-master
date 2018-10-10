USER_TYPE_CHOICES = (

    ('seller', 'seller'), ('buyer', 'buyer'), ('lessor', 'lessor'), ('tenant', 'tenant')
)

POST_CHOICES = (

    ('Sale', 'Sale'), ('Rent', 'Rent')

)

PROPERTY_TYPE_CHOICES = (

    ('Flat', 'Flat'), ('House/Villa', 'House/Villa'),
    ('Plot', 'Plot'), ('Office Space', 'Office Space'),
    ('Other Commercial', 'Other Commercial'),
    ('Shop/Showroom', 'Shop/Showroom'), ('PG', 'PG')

)

BHK_CHOICES = (

    ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('>5', '>5')

)

CONSTRUCTION_STATUS_CHOICES = (

    ('Under Construction', 'Under Construction'), ('Ready To Move', 'Ready To Move')

)
