import { FC, ReactNode } from 'react';
import { IconBox, IconInformation, IconWarningTriangle } from '@robocorp/icons/iconic';
import {
  IconAtSign,
  IconEmptyCircle,
  IconFrame,
  IconPauseCircle,
  IconPlayCircle,
  IconStatusCompleted,
  IconStatusError,
  IconStatusIdle,
} from '@robocorp/icons';
import { Badge, Box } from '@robocorp/components';

import {
  Entry,
  EntryException,
  EntryMethodBase,
  EntryResumeYield,
  EntryResumeYieldFrom,
  EntryTask,
  StatusLevel,
  Type,
} from '~/lib/types';
import { Color } from '@robocorp/theme/types';

type Props = {
  entry: Entry;
};

const getLogIcon = (status: StatusLevel): ReactNode => {
  switch (status) {
    case StatusLevel.error:
      return <IconStatusError color="background.error" />;
    case StatusLevel.warn:
      return <IconWarningTriangle color="background.notification" />;
    case StatusLevel.info:
      return <IconStatusIdle color="background.accent" />;
    case StatusLevel.success:
      return <IconStatusCompleted color="background.success" />;
    case StatusLevel.unset:
      return <IconEmptyCircle color="background.notification" />;
    default:
      return <IconInformation color="blue60" />;
  }
};
function getColorFromStatus(status: StatusLevel): Color {
  let useColor: Color = 'background.success';
  switch (status) {
    case StatusLevel.error:
      useColor = 'background.error';
      break;
    case StatusLevel.warn:
      useColor = 'background.notification';
      break;
    case StatusLevel.info:
      useColor = 'background.accent';
      break;
    case StatusLevel.unset:
      useColor = 'background.success';
  }
  return useColor;
}

const getTaskIcon = (status: StatusLevel): ReactNode => {
  return <IconAtSign color={getColorFromStatus(status)} size="small" />;
};

const getGeneratorIcon = (status: StatusLevel): ReactNode => {
  return <IconPlayCircle color={getColorFromStatus(status)} size="small" />;
};

const getUntrackedGeneratorIcon = (): ReactNode => {
  // Note that we don't have a status for an untracked generator.
  return <IconFrame color="background.success" size="small" />;
};

const getResumeYieldIcon = (status: StatusLevel): ReactNode => {
  // Note that we don't have a status for an untracked generator.
  return <IconPlayCircle color={getColorFromStatus(status)} size="small" />;
};

const getSuspendYieldIcon = (): ReactNode => {
  return <IconPauseCircle color="magenta60" size="small" />;
};

const getIcon = (entry: Entry): ReactNode => {
  switch (entry.type) {
    case Type.task:
      const entryTask: EntryTask = entry as EntryTask;
      return getTaskIcon(entryTask.status);
    case Type.method:
      return getLogIcon((entry as EntryMethodBase).status);
    case Type.generator:
      return getGeneratorIcon((entry as EntryMethodBase).status);
    case Type.untrackedGenerator:
      return getUntrackedGeneratorIcon();
    case Type.resumeYield:
    case Type.resumeYieldFrom:
      return getResumeYieldIcon((entry as EntryResumeYield | EntryResumeYieldFrom).status);
    case Type.suspendYield:
    case Type.suspendYieldFrom:
      return getSuspendYieldIcon();
    case Type.variable:
      return <IconBox color="blue60" size="small" />;
    case Type.exception:
      const exc: EntryException = entry as EntryException;
      return (
        <Badge
          icon={IconStatusError}
          variant="danger"
          iconColor="background.error"
          label={exc.excType}
          size="small"
        />
      );
    default:
      return <IconInformation color="blue60" />;
  }
};

export const Icon: FC<Props> = ({ entry }) => {
  return (
    <Box display="flex" alignItems="center" height="$32" mr="$8">
      {getIcon(entry)}
    </Box>
  );
};
