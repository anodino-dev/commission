import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-commission",
    description="Meta package for oca-commission Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-sale_commission',
        'odoo10-addon-sale_commission_areamanager',
        'odoo10-addon-sale_commission_formula',
        'odoo10-addon-sale_commission_geo_assign',
        'odoo10-addon-sale_commission_pricelist',
        'odoo10-addon-website_sale_commission_lead_geo_assign',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
