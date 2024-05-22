import { ServiceTemplate } from '@/client';

export const SERVICE_TEMPLATES: ServiceTemplate[] = [
  {
    name: 'Trader Agent',
    hash: 'bafybeiha6dxygx2ntgjxhs6zzymgqk3s5biy3ozeqw6zuhr6yxgjlebfmq',
    description: 'Trader agent for omen prediction markets',
    image:
      'https://operate.olas.network/_next/image?url=%2Fimages%2Fprediction-agent.png&w=3840&q=75',
    configuration: {
      nft: 'bafybeig64atqaladigoc3ds4arltdu63wkdrk3gesjfvnfdmz35amv7faq',
      agent_id: 14,
      threshold: 1,
      use_staking: true,
      cost_of_bond: 10000000000000000,
      olas_cost_of_bond: 10000000000000000000,
      olas_required_to_stake: 10000000000000000000,
      monthly_gas_estimate: 22500000000000000000,
      fund_requirements: {
        agent: 100000000000000000,
        safe: 5000000000000000000,
      },
    },
  },
];
