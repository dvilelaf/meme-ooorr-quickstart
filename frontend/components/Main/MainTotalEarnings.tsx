import { Typography } from 'antd';

import { balanceFormat } from '@/common-util/numberFormatters';

const earnings = 0;
export const MainTotalEarnings = () => {
  return (
    <Typography.Text>
      Total earnings: {balanceFormat(earnings, 2)} OLAS
    </Typography.Text>
  );
};
