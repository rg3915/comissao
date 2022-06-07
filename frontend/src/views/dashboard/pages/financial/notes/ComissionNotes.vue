<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Notas de Pagamento da Comissão"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Funcionário
            </th>
            <th class="primary--text text-center">
              Data
            </th>
            <th class="primary--text text-right">
              Valor
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
            <td>
              <a href="#/pages/financial/comission-note">{{ item.employee }}</a>
            </td>
            <td class="text-center">
              {{ item.payment_date }}
            </td>
            <td>R$ <span class="float-right">{{ item.value }}</span></td>
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
            employee: 'Brenda Lawson',
            payment_date: '30/10/2020',
            value: 680.99,
          },
          {
            employee: 'Christopher Mcpherson',
            payment_date: '30/10/2020',
            value: 670.99,
          },
          {
            employee: 'Crystal Snyder',
            payment_date: '30/10/2020',
            value: 700.99,
          },
          {
            employee: 'David Valentine',
            payment_date: '30/10/2020',
            value: 980.99,
          },
          {
            employee: 'Donna Smith',
            payment_date: '30/10/2020',
            value: 1250.99,
          },
          {
            employee: 'Jason Schmidt',
            payment_date: '30/10/2020',
            value: 354.99,
          },
          {
            employee: 'John Williams',
            payment_date: '30/10/2020',
            value: 320.99,
          },
          {
            employee: 'Michelle Hill',
            payment_date: '30/10/2020',
            value: 1380.99,
          },
        ],
      }
    },
  }
</script>
