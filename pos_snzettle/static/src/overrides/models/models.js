/** @thrive-module */

import { register_payment_method } from "@point_of_sale/app/store/pos_store";
import { PaymentSNZettle } from "@pos_snzettle/app/payment_snzettle";

register_payment_method("snzettle", PaymentSNZettle);

