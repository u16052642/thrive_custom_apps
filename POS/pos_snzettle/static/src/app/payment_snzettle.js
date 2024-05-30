/** @thrive-module */

import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";
import { PaymentInterface } from "@point_of_sale/app/payment/payment_interface";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { escape } from "@web/core/utils/strings";

export class PaymentSNZettle extends PaymentInterface {
    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    addCss() {
        const customModalStyles = `
            /* Modal styles */
            .sn-zettle-modal-text {
                width: 380px;
                text-align: center;
            }
            .sn-zettle-modal {
                display: inline-block;
                position: fixed;
                z-index: 1000;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.5);
            }

            .sn-zettle-modal-content {
                background-color: #fff;
                border-radius: 5px;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                padding: 20px;
            }

            /* Button styles */
            .sn-zettle-modal-button {
                padding: 10px 20px;
                margin: 5px;
                cursor: pointer;
                font-size: 16px;
            }
            /* Modal styles */
            .sn-zettle-promo-modal-text {
                text-align: center;
            }
            .sn-zettle-promo-modal {
                display: inline-block;
                position: fixed;
                z-index: 1000;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.5);
            }

            .sn-zettle-promo-modal-content {
                background-color: #fff;
                border-radius: 5px;
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                padding: 20px;
            }

            /* Button styles */
            .sn-zettle-promo-modal-button {
                padding: 10px 20px;
                margin: 5px;
                cursor: pointer;
                font-size: 16px;
            }
        `;

        // Create a <style> element and append it to the document's <head>
        const styleElement = document.createElement('style');
        styleElement.innerHTML = customModalStyles;
        document.head.appendChild(styleElement);
    }
    displayModal(self, deviceType) {
            var currentURL = window.location.href;
            var encodedURL = encodeURIComponent(currentURL);
            const modal = document.createElement('div');
            modal.classList.add('sn-zettle-modal');
            modal.innerHTML = `
                <div class="sn-zettle-modal-content">
                    <h2 class="sn-zettle-modal-text">Open SN Zettle POS?</h2>
                    <p class="sn-zettle-modal-text">Please select a payment type:</p>
                    <button class="sn-zettle-modal-button" id="btnCard">Card</button>
                    <button class="sn-zettle-modal-button" id="btnPayPal">PayPal</button>
                    <button class="sn-zettle-modal-button" id="btnVenmo">Venmo</button>
                    <button class="sn-zettle-modal-button" id="btnCancel">Cancel</button>
                </div>
            `;

            // Add the modal to the document body
            document.body.appendChild(modal);

            // Function to close the modal
            function closeModal() {
                document.body.removeChild(modal);
            }

            // Event listeners for button clicks
            document.getElementById("btnCard").addEventListener("click", function() {
                if(deviceType === "android") {
                    window.open("app://sn-zettle-payment-android?paymentType=0&redirectUrl=" + encodedURL);
                }
                else {
                    //window.open("snzettle://payment?paymentType=card", '_blank');
                    window.webkit.messageHandlers.btnCard.postMessage(null);
                }
                closeModal();
            });

            document.getElementById("btnPayPal").addEventListener("click", function() {
                if(deviceType === "android") {
                    window.open("app://sn-zettle-payment-android?paymentType=2&redirectUrl=" + encodedURL);
                }
                else {
                    //window.open("snzettle://payment?paymentType=paypal", '_blank');
                    window.webkit.messageHandlers.btnPayPal.postMessage(null);
                }
                closeModal();
            });

            document.getElementById("btnVenmo").addEventListener("click", function() {
                if(deviceType === "android") {
                    window.open("app://sn-zettle-payment-android?paymentType=1&redirectUrl=" + encodedURL);
                }
                else {
                    //window.open("snzettle://payment?paymentType=venmo", '_blank');
                    window.webkit.messageHandlers.btnVenmo.postMessage(null);
                }
                closeModal();
            });

            document.getElementById("btnCancel").addEventListener("click", function() {
                closeModal();
            });
    }

    displayPromotionModal(self) {
        var promoModal = document.createElement('div');
        promoModal.classList.add('sn-zettle-promo-modal');
        promoModal.innerHTML = `
            <div class="sn-zettle-promo-modal-content">
                <h2 class="sn-zettle-promo-modal-text">Welcome to SN Zettle!</h2>
                <p class="sn-zettle-promo-modal-text">Thank you for installing SN Zettle POS. We hope you enjoy our app and if you do please leave a positive review!</p>
                <p class="sn-zettle-promo-modal-text">Don't have a Zettle <b>account</b> yet? We are not just a pretty face we can get you a <b>GREAT DEAL</b> as well! Please select one of the options below: </p>
                <button class="sn-zettle-promo-modal-button" id="btnDeal">Yes please I want a great deal</button>
                <button class="sn-zettle-promo-modal-button" id="btnRemindMe">Remind me later</button>
                <button class="sn-zettle-promo-modal-button" id="btnAccountExists">I already have an account</button>
            </div>
        `;
        document.body.appendChild(promoModal);

        function closeModal() {
            document.body.removeChild(promoModal);
        }
        var rpc = this.env.services.rpc
        document.getElementById("btnDeal").addEventListener("click", function() {
            if(window.isSNZettleiOSApp) {
                window.webkit.messageHandlers.btnDeal.postMessage(null);
            }
            else {
                window.open("https://www.simply-neat.com/zettle-sign-up");
            }
            rpc('/pos_zettle/promotion_displayed',{})
            .then(() => {
                closeModal();
            })
        });

        document.getElementById("btnRemindMe").addEventListener("click", function() {
            closeModal();
        });

        document.getElementById("btnAccountExists").addEventListener("click", function() {
            rpc('/pos_zettle/promotion_displayed',{})
            .then(() => {
                closeModal();
            })
        });
    }
    /**
     * @override
    */
    setup() {
        super.setup(...arguments);
        if(!window.hasRenderedPromotion) {
            window.hasRenderedPromotion = false
        }
        this.addCss()
        if(window.hasRenderedPromotion === false) {
            window.hasRenderedPromotion = true
            this.env.services.rpc('/pos_zettle/has_promotion_displayed',{}).then(res => {
                if(res && res.data && res.data.promotion_displayed === false) {
                    this.setupRenderCount++
                    setTimeout(() => this.displayPromotionModal(this), 5000);
                }
            })
        }
    }
    /**
     * @override
    */
    async send_payment_request (cid) {
        super.send_payment_request(...arguments);
        const line = this.pos.get_order().selected_paymentline;
        const order = this.pos.get_order();
        const data = this._terminal_pay_data();
        const terminalId = data.PaymentMethod.sn_zettle_terminal_device_code
        const refunded_order_line_ids = []

        for(let i = 0; i < order.orderlines.length; i++) {
            var orderline = order.orderlines[i]
            if(orderline.refunded_orderline_id) {
                refunded_order_line_ids.push(orderline.refunded_orderline_id)
            }
        }

        if(refunded_order_line_ids.length > 1) {
            const iosr = await this.env.services.rpc('/pos_zettle/is_order_the_same', {
                    refunded_order_line_ids
            })

            if(!iosr || !iosr.data || !iosr.data.is_order_the_same) {
                line.set_payment_status('retry');
                throw new Error('Cannot have multiple refunds in an order.');
                return
            }
        }

        var refunded_order_line_id = undefined
        if(refunded_order_line_ids.length) {
            refunded_order_line_id = refunded_order_line_ids[0]
        }

        const params = {
            terminal_id: terminalId,
            order_id: data.OrderID,
            amount: data.RequestedAmount,
            user_id: order.cashier.id,
            refunded_order_line_id,
        }

        const result = await this.env.services.rpc('/pos_zettle/create_payment_request', params)
        if(!result || result.status === 403 || result.status === 400) {
            line.set_payment_status('retry');
            return false
        }
        const device = window.navigator.userAgent
        const isMobile = device.includes("Android") || window.isSNZettleiOSApp
        if(result && result.status === 201 && data.PaymentMethod.sn_zettle_is_mobile && isMobile) {
          if(data.PaymentMethod.sn_zettle_device_type === 'android') {
            this.displayModal(this, data.PaymentMethod.sn_zettle_device_type)
          }
          else {
            if(window.isSNZettleiOSApp) {
                this.displayModal(this, data.PaymentMethod.sn_zettle_device_type)
            }
          }
        }
        line.set_payment_status('waitingCard');
        while(true) {
            const res = await this.env.services.rpc('/pos_zettle/check_request', {
                terminal_id: terminalId,
                transaction_id: result.data.transaction_id,
            })

            if(res && res.status === 200) {
                if(res.data.status === 'done' || res.data.status === 'refunded' || res.data.status === 'resent_done' || res.data.status === 'resent_refunded') {
                    const processed_result = await this.env.services.rpc('/pos_zettle/request_processed', {
                        terminal_id: terminalId,
                        transaction_id: res.data.transaction_id,
                    })
                    if(processed_result && processed_result.status == 200) {
                        line.transaction_id = res.data.transaction_id;
                        line.card_type = res.data.card_type;
                        line.cardholder_name = res.data.cardholder_name
                        if(res.data.is_refund && line.amount !== res.data.refunded_amount) {
                            if(res.data.refunded_amount < 0) {
                                line.amount = res.data.refunded_amount
                            }
                            else {
                                line.amount = -1 * res.data.refunded_amount
                            }
                        }
                        else {
                            line.amount = res.data.transaction_amount
                        }
                        line.set_payment_status('done');
                        return true
                    }
                }
                else if(res.data.status !== 'pending') {
                    line.set_payment_status('retry');
                    return false
                }
            }
            else {
                line.set_payment_status('retry');
                return false
            }
            await this.sleep(2000)
        }
        return true
    }
    /**
     * @override
    */
    async send_payment_cancel() {
        super.send_payment_cancel(...arguments);
        console.log('cancel')
        const line = this.pos.get_order().selected_paymentline;
        const data = this._terminal_pay_data();
        const terminalId = data.PaymentMethod.sn_zettle_terminal_device_code
        while(true) {
            try {
                const res = await this.env.services.rpc('/pos_zettle/cancel_payment_request', {
                    terminal_id: terminalId,
                    order_id: data.OrderID,
                })
                if(res && res.status) {
                    break
                }
            }
            catch(e) {
                continue
            }
        }
        return true;
    }
    _terminal_pay_data() {
          const order = this.pos.get_order();
          const line = order.selected_paymentline;
          const data = {
                'Name': order.name,
                'OrderID': order.uid,
                'Currency': this.pos.currency.name,
                'RequestedAmount': line.amount,
                'PaymentMethod': this.payment_method
          };
         return data;
    }
}


