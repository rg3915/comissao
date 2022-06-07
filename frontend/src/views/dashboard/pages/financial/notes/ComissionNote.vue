<template>
  <v-container
    id="comission-note"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Nota de Pagamento da Comissão: Dakota Rice"
      class="px-5 py-3"
    >
      <v-form>
        <v-container class="py-0">
          <v-row>
            <v-col
              cols="12"
              md="4"
            >
              <v-text-field
                label="Funcionário"
                value="Dakota Rice"
                disabled
              />
            </v-col>

            <v-col
              cols="12"
              md="4"
            >
              <v-text-field
                label="Data Inicial"
                value="01/11/2020"
              />
            </v-col>

            <v-col
              cols="12"
              md="4"
            >
              <v-text-field
                label="Data Final"
                value="30/11/2020"
              />
            </v-col>
          </v-row>
        </v-container>
      </v-form>
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Pedido
            </th>
            <th class="text-center primary--text">
              Quantidade
            </th>
            <th class="primary--text">
              Serviço
            </th>
            <th class="text-right primary--text">
              Valor da comissão
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="item in items"
            :key="item.order"
          >
            <td>{{ item.order }}</td>
            <td class="text-center">
              {{ item.quantity }}
            </td>
            <td>{{ item.description }}</td>
            <td><span class="float-right">R$ {{ item.value }}</span></td>
          </tr>
        </tbody>

        <tfoot>
          <tr>
            <td class="text-h3 font-weight-light text--primary">
              <small>Pago?</small> <v-icon
                class="mx-1"
                style="color: green"
              >
                mdi-check-bold
              </v-icon>
            </td>
            <td class="text-center">
              Data de pagto: 01/11/2020
            </td>
            <td class="text-h3 text-right">
              Total
            </td>
            <td class="text-h2">
              <span class="float-right">R$ 106,68</span>
            </td>
          </tr>
        </tfoot>
      </v-simple-table>
    </base-material-card>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        items: [
          {
            order: '001',
            quantity: 1,
            description: 'Corte cabelo',
            value: 12.55,
          },
          {
            order: '001',
            quantity: 1,
            description: 'Maquiagem',
            value: 12.01,
          },
          {
            order: '002',
            quantity: 1,
            description: 'Sobrancelha',
            value: 18.99,
          },
          {
            order: '002',
            quantity: 1,
            description: 'Mão e Pé',
            value: 27.05,
          },
          {
            order: '003',
            quantity: 1,
            description: 'Depilação',
            value: 36.08,
          },
        ],
      }
    },
  }
</script>
