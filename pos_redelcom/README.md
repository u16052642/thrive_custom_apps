# POS Redelcom

Integrate your POS with a Redelcom payment terminal.

## Configuration

### Setting Up Payment Method

- Navigate to *Point of Sale > Configuration > Payment Methods*.
- Create a new payment method.
- Select *Redelcom* from the list of available payment terminals.
- Enter your Redelcom credentials.
- Save the payment method and verify that the *Redelcom Terminal Code* field is automatically populated.

![image_01.png](static/description/image_01.png)

Note: Set *Redelcom Mode* as demo if you only want to make payments in the test environment.

### Enabling the Payment Method

- Access *Point of Sale > Configuration > Settings*.
- Activate the Redelcom payment method for each point of sale where it will be utilized.

![image_02.png](static/description/image_02.png)

## Usage

### Using the Redelcom Payment Method

- At the point of sale interface, select the items for purchase.
- When ready to make a payment, choose the Redelcom payment method.
- A button will appear allowing you to send the transaction to the Redelcom payment terminal.
- Complete the transaction on the Redelcom terminal as necessary.

![image_03.png](static/description/image_03.png)

### Verifying Transaction Status

- Access *Point of Sale > Orders > Payment Status*.
- Select the payment method associated with the Redelcom terminal.
- Consult the transaction number to verify the status of a transaction.

![image_04.png](static/description/image_04.png)

Note: This menu is enabled only for users with a point of sale administrator profile.

## Known issues

This module has been tested exclusively with the Redelcom A910 payment terminal.

For more information about compatible devices and troubleshooting, please refer to the following [link](https://www.mercadopago.cl/herramientas-para-vender/lectores-point/point-smart?device=101&code=POINT_POM).

## Credits

### Authors

- Konos Soluciones & Servicios

### Contributors

- Alexander Olivares <<aolivares@konos.cl>>
