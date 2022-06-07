<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Pagamentos"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Descrição
            </th>
            <th class="primary--text">
              Cliente
            </th>
            <th class="primary--text">
              Valor
            </th>
            <th class="primary--text">
              Data de Pagamento
            </th>
            <th class="primary--text">
              Data de Vencimento
            </th>
            <th class="primary--text">
              Tipo de Pagamento
            </th>
            <th class="primary--text">
              Pago?
            </th>
            <th class="text-right primary--text">
              Editar
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="item in items"
            :key="item"
          >
            <td>{{ item.description }}</td>
            <td>{{ item.customer }}</td>
            <td>R$ <span class="float-right">{{ item.value }}</span></td>
            <td>{{ item.payment_date }}</td>
            <td>{{ item.expiration_date }}</td>
            <td>{{ item.expense_type }}</td>
            <td v-if="item.paid">
              <v-icon
                class="mx-1"
                style="color: green"
              >
                mdi-check
              </v-icon>
            </td>
            <td v-else>
              <v-icon
                class="mx-1"
                style="color: red"
              >
                mdi-close
              </v-icon>
            </td>
            <td class="text-right">
              <v-icon class="mx-1">
                mdi-pencil
              </v-icon>
            </td>
          </tr>
        </tbody>
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
            description: 'Pagamento do Pedido 001',
            payment_date: '26/10/2020',
            expiration_date: '26/10/2020',
            customer: 'Dakota Rice',
            expense_type: 'atendimento',
            value: 119.99,
            paid: true,
          },
          {
            description: 'Pagamento do Pedido 002',
            payment_date: '26/10/2020',
            expiration_date: '26/10/2020',
            customer: 'Priscilla Campbell',
            expense_type: 'atendimento',
            value: 110.99,
            paid: true,
          },
          {
            description: 'Pagamento do Pedido 003',
            payment_date: '26/10/2020',
            expiration_date: '26/10/2020',
            customer: 'Joana Rizzo',
            expense_type: 'atendimento',
            value: 189.99,
            paid: true,
          },
          {
            description: 'Pagamento do Pedido 004',
            payment_date: '26/10/2020',
            expiration_date: '26/10/2020',
            customer: 'Brenda Lawson',
            expense_type: 'atendimento',
            value: 310.99,
            paid: true,
          },
          {
            description: 'Pagamento do Pedido 005',
            payment_date: '',
            expiration_date: '25/10/2020',
            customer: 'Dakota Rice',
            expense_type: 'atendimento',
            value: 200.99,
            paid: false,
          },
        ],
      }
    },
  }
</script>
