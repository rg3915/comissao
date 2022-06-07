<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Despesas"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Descrição
            </th>
            <th class="primary--text">
              Data de Pagamento
            </th>
            <th class="primary--text">
              Data de Vencimento
            </th>
            <th class="primary--text">
              Pago à
            </th>
            <th class="primary--text">
              Tipo de Despesa
            </th>
            <th class="primary--text">
              Valor
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
            <td>{{ item.payment_date }}</td>
            <td>{{ item.expiration_date }}</td>
            <td>{{ item.customer }}</td>
            <td>{{ item.expense_type }}</td>
            <td>R$ <span class="float-right">{{ item.value }}</span></td>
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
            description: 'Aluguel',
            payment_date: '26/10/2020',
            expiration_date: '26/10/2020',
            customer: 'John Williams',
            expense_type: 'Imóvel',
            value: 2400.01,
            paid: true,
          },
          {
            description: 'Internet',
            payment_date: '26/10/2020',
            expiration_date: '26/10/2020',
            customer: 'Best Net',
            expense_type: 'Comunicação',
            value: 110.15,
            paid: true,
          },
          {
            description: 'Luz',
            payment_date: '26/10/2020',
            expiration_date: '26/10/2020',
            customer: 'Light Energy',
            expense_type: 'Consumo',
            value: 189.99,
            paid: true,
          },
          {
            description: 'Água',
            payment_date: '26/10/2020',
            expiration_date: '26/10/2020',
            customer: 'Wather Forever',
            expense_type: 'Consumo',
            value: 310.22,
            paid: true,
          },
          {
            description: 'Celular',
            payment_date: '26/10/2020',
            expiration_date: '26/10/2020',
            customer: 'J2 Telecom',
            expense_type: 'Comunicação',
            value: 200.14,
            paid: true,
          },
        ],
      }
    },
  }
</script>
