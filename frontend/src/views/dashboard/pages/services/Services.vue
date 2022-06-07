<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <v-btn
      tile
      color="primary"
      @click="goToCustomerAdd()"
    >
        <v-icon left>
          mdi-plus
        </v-icon>
        Adicionar
    </v-btn>
    <base-material-card
      icon="mdi-clipboard-text"
      title="Serviços"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Descrição
            </th>
            <th class="primary--text">
              Preço
            </th>
            <th class="primary--text text-center">
              Comissão
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="item in items"
            :key="item"
          >
            <td>
              <router-link :to="{ name: 'Serviço', params: { id: item.id }}">{{ item.description }}</router-link>
            </td>
            <td style="width:150px">R$ <span class="float-right">{{ item.price }}</span></td>
            <td class="text-center">{{ item.comission|percentage }}%</td>
          </tr>
        </tbody>
      </v-simple-table>
    </base-material-card>
  </v-container>
</template>

<script>
  import axios from 'axios'

  export default {
    data () {
      return {
        items: [
          {
            description: 'Corte cabelo',
            price: 45.15,
            comission: 0.3,
          },
          {
            description: 'Maquiagem',
            price: 39.99,
            comission: 0.3,
          },
          {
            description: 'Sobrancelha',
            price: 65.19,
            comission: 0.3,
          },
          {
            description: 'Mão e Pé',
            price: 90.09,
            comission: 0.3,
          },
          {
            description: 'Depilação',
            price: 120.99,
            comission: 0.3,
          },
        ],
      }
    },
    mounted () {
      this.getData()
    },
    methods: {
      getData () {
        axios.get('/api/v1/services/')
          .then(response => {
            if (response.data.length) {
              this.items = response.data
            }
          })
      },
      goToCustomerAdd () {
        this.$router.push({ name: 'Adicionar Serviço' })
      },
    },
    filters: {
      percentage (comission) {
        return comission * 100
      },
    },
  }
</script>
