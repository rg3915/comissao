<template>
  <v-container
    id="user-profile"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        md="8"
      >
        <base-material-card>
          <template v-slot:heading>
            <div class="text-h3 font-weight-light">
              Adicionar Pedido
            </div>

            <!-- <div class="text-subtitle-1 font-weight-light">
            </div> -->
          </template>

          <v-form @submit.prevent="submitForm">
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="12"
                  md="6"
                >
                  <v-text-field
                    v-model="total"
                    class="purple-input"
                    label="Valor"
                    disabled
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="6"
                >
                  <v-checkbox
                    v-model="item.paid"
                    label="Pago?"
                  ></v-checkbox>
                </v-col>

                <v-col
                  cols="12"
                  md="12"
                >
                <v-select
                  v-model="item.customer"
                  label="Cliente"
                  :items="customers"
                  ></v-select>
                </v-col>

                <v-col
                  cols="12"
                  class="text-right"
                >
                  <v-btn
                    color="success"
                    class="mr-0"
                    type="submit"
                  >
                    Salvar
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>

        </base-material-card>

        <base-material-card>
          <template v-slot:heading>
            <div class="text-h3 font-weight-light">
              Itens do Pedido
            </div>
          </template>

          <v-simple-table>
            <thead>
              <tr>
                <th class="text-center primary--text">
                  Quantidade
                </th>
                <th class="primary--text">
                  Serviço
                </th>
                <th class="text-right primary--text">
                  Preço
                </th>
                <th class="primary--text">
                  Funcionário
                </th>
                <th class="text-right primary--text">
                  Comissão
                </th>
              </tr>
            </thead>

            <tbody>
              <tr
                v-for="(subitem, idx) in item.order_items"
                :key="subitem.id"
              >
                <td class="text-center">
                  <v-text-field
                    v-model="item.order_items[idx].quantity"
                    label="Quantidade"
                  />
                </td>
                <td>
                  <v-select
                  v-model="item.order_items[idx].service"
                  label="Serviço"
                  :items="services"
                  @change="getPrice(item.order_items[idx].service, idx)"
                  ></v-select>
                </td>
                <td>
                  <v-text-field
                    v-model="item.order_items[idx].price"
                    label="Preço"
                  />
                </td>
                <td>
                  <v-select
                  v-model="item.order_items[idx].employee"
                  label="Funcionário"
                  :items="employees"
                  ></v-select>
                </td>
                <td class="text-right">
                  <v-text-field
                    v-model="item.order_items[idx].comission_employee"
                    label="Comissão"
                  />
                </td>
              </tr>
            </tbody>

            <tfoot>
              <tr>
                <td colspan="5">
                  <v-btn
                    color="primary"
                    class="mr-0 float-right"
                    @click="addOrderItem()"
                  >
                    <v-icon left>
                      mdi-plus
                    </v-icon>
                    Adicionar
                  </v-btn>
                </td>
              </tr>
            </tfoot>
          </v-simple-table>
        </base-material-card>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        customers: [],
        employees: [],
        services: [],
        services_obj: [],
        item: {
          value: '',
          paid: false,
          customer: '',
          order_items: [],
        },
      }
    },
    mounted () {
      this.getCustomers()
      this.getEmployees()
      this.getServices()
    },
    computed: {
      total: function () {
        return this.item.order_items.reduce((acc, item) => acc + parseFloat(item.price), 0)
      },
    },
    methods: {
      getCustomers () {
        axios.get('/api/v1/customers')
          .then(response => {
            this.customers = response.data.map(obj => {
              return {
                value: obj.id,
                text: `${obj.first_name} ${obj.last_name}`,
              }
            })
          })
      },
      getEmployees () {
        axios.get('/api/v1/employees')
          .then(response => {
            this.employees = response.data.map(obj => {
              return {
                value: obj.id,
                text: `${obj.user.first_name} ${obj.user.last_name}`,
              }
            })
          })
      },
      getServices () {
        axios.get('/api/v1/services')
          .then(response => {
            this.services = response.data.map(obj => {
              return {
                value: obj.id,
                text: obj.description,
              }
            })
            this.services_obj = response.data
          })
      },
      getPrice (serviceId, idx) {
        const data = this.services_obj.find(i => i.id === serviceId)
        this.item.order_items[idx].price = data.price
        this.item.order_items[idx].comission_employee = data.comission
      },
      addOrderItem () {
        this.item.order_items.push({
          quantity: '',
          service: '',
          price: '',
          employee: '',
          comission_employee: '',
        })
      },
      async submitForm () {
        const item = { ...this.item }
        item.value = this.total
        // Se quiser editar o Valor total manualmente, ignore o Spread operator (const item = { ...this.item })
        // e faça .post('/api/v1/orders/', this.item).
        axios
          .post('/api/v1/orders/', item)
          .then(() => {
            this.$router.push({ name: 'Pedidos' })
          })
          .catch(error => {
            console.log(error)
          })
      },
    },
  }
</script>
