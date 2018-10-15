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

PROPERTY_TYPE_CHOICES_FILTER = (

    ('No Preference', 'No Preference'), ('Flat', 'Flat'), ('House/Villa', 'House/Villa'),
    ('Plot', 'Plot'), ('Office Space', 'Office Space'),
    ('Other Commercial', 'Other Commercial'),
    ('Shop/Showroom', 'Shop/Showroom'), ('PG', 'PG')

)

BHK_CHOICES = (

    ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('>5', '>5')

)

BHK_CHOICES_FILTER = (

    ('No Preference', 'No Preference'), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
    ('>5', '>5')

)

CONSTRUCTION_STATUS_CHOICES = (

    ('Ready To Move', 'Ready To Move'), ('Under Construction', 'Under Construction')

)

CONSTRUCTION_STATUS_CHOICES_FILTER = (

    ('No Preference', 'No Preference'), ('Ready To Move', 'Ready To Move'), ('Under Construction', 'Under Construction')

)

PRICE_CHOICES = (

    ('1-2L', '1-2L'), ('2-10L', '2-10L'), ('10-20L', '10-20L'), ('20-30L', '20-30L'), ('30-50L', '30-50L'),
    ('50L-1Cr', '50L-1Cr'), ('1', '2Cr'), ('2-3Cr', '2-3Cr'), ('3-5Cr', '3-5Cr'), ('>5Cr', '>5Cr')

)

PRICE_CHOICES_FILTER = (

    ('No Preference', 'No Preference'), ('1-2L', '1-2L'), ('2-10L', '2-10L'), ('10-20L', '10-20L'),
    ('20-30L', '20-30L'), ('30-50L', '30-50L'),
    ('50L-1Cr', '50L-1Cr'), ('1', '2Cr'), ('2-3Cr', '2-3Cr'), ('3-5Cr', '3-5Cr'), ('>5Cr', '>5Cr')

)

AREA_CHOICES = (

    ('100-200sqft', '100-200sqft'), ('200-400sqft', '200-400sqft'), ('400-600sqft', '400-600sqft'),
    ('600-800sqft', '600-800sqft'), ('800-1000sqft', '800-1000sqft'), ('1000-2000sqft', '1000-2000sqft'),
    ('2000-3000sqft', '2000-3000sqft'), ('3000-4000sqft', '3000-4000sqft'), ('4000-5000sqft', '4000-5000sqft'),
    ('>5000sqft', '>5000sqft'),

)

AREA_CHOICES_FILTER = (

    ('No Preference', 'No Preference'), ('100-200sqft', '100-200sqft'), ('200-400sqft', '200-400sqft'),
    ('400-600sqft', '400-600sqft'),
    ('600-800sqft', '600-800sqft'), ('800-1000sqft', '800-1000sqft'), ('1000-2000sqft', '1000-2000sqft'),
    ('2000-3000sqft', '2000-3000sqft'), ('3000-4000sqft', '3000-4000sqft'), ('4000-5000sqft', '4000-5000sqft'),
    ('>5000sqft', '>5000sqft'),

)
