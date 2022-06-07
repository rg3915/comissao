<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Pedidos"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Nº
            </th>
            <th class="primary--text">
              Cliente
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
            <td>
              <a href="#/pages/services/order">{{ item.number }}</a>
            </td>
            <td>{{ item.customer }}</td>
            <td>R$ <span class="float-right">{{ item.value }}</span></td>
            <td v-if="item.paid">
              <v-icon
                class="mx-1"
                style="color: green"
              >
                mdi-check-bold
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
            number: '001',
            customer: 'Dakota Rice',
            value: 180.00,
            paid: true,
          },
          {
            number: '002',
            customer: 'Priscila Jones',
            value: 220.00,
            paid: true,
          },
          {
            number: '003',
            customer: 'Sage Rodriguez',
            value: 110.00,
            paid: true,
          },
          {
            number: '004',
            customer: 'Philip Chaney',
            value: 90.00,
            paid: false,
          },
          {
            number: '005',
            customer: 'Doris Green',
            value: 200.00,
            paid: false,
          },
        ],
      }
    },
  }
</script>
